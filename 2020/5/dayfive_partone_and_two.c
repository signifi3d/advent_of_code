#include <stdio.h>

int max_seat_id(const unsigned char seats[]) {
	//Count down from the max possible seat id, when a filled seat is found that is the max seat id
	for (int curr_id = 1023; curr_id >= 0; --curr_id) 
		if ((seats[curr_id/8] >> (curr_id%8)) & 1)
			return curr_id;
	return -1;
}

int find_seat_id(const unsigned char seats[]) {
	//Count up from the lowest seat id, check for seats where the bit is not set, but the surrounding ones are
	for(int curr_id = 1; curr_id < 1023; ++curr_id) 
		if ((seats[(curr_id-1)/8] >> ((curr_id-1)%8) & 1) && !((seats[curr_id/8] >> (curr_id%8)) & 1) && ((seats[(curr_id+1)/8] >> ((curr_id+1)%8)) & 1))
			return curr_id;
	return -1;
}

int main() {

	FILE * fd;
	ssize_t read_res;
	size_t read_len = 0;
	char * line = NULL;

	unsigned char seats[128] = {0};
	unsigned __int128 curr_row;
	unsigned char curr_shift, curr_seat, row_index = 0;

	fd = fopen("input.txt", "r");

	//Fill in all of the occupied seats
	while ((read_res = getline(&line, &read_len, fd)) != -1) {
		curr_shift = 64;
		//gcc doesn't allow 128-bit constants, so you have to intialize it in two steps
		curr_row = 0xffffffffffffffff;
		curr_row = curr_row << 64;
		curr_row |= 0xffffffffffffffff;
		row_index = 0;
		
		//The idea is that each bit in the 128-bit int represents a different row
		//We can represent F and B as shifts of decreasing powers of 2
		for (int i = 0; i < 7; ++i) {
			if (line[i] == 'F') {
				curr_row &= curr_row >> curr_shift;
			} else if (line[i] == 'B') {
				curr_row &= curr_row << curr_shift;
			} else {
				printf("Invalid row assignment character %c\n", line[i]);
				return 1;
			}

			curr_shift = curr_shift >> 1;
		}
		
		//Find the index corresponding to the row bit
		while ((curr_row & 0x1) == 0) {
			++row_index;
			curr_row = curr_row >> 1;
		}

		//reset seat variables
		curr_shift = 4;
		curr_seat = 0xff;

		//Same idea with the seats as the rows
		for (int i = 7; i < 10; ++i) {
			if (line[i] == 'R') {
				curr_seat &= curr_seat << curr_shift;
			} else if (line[i] == 'L') {
				curr_seat &= curr_seat >> curr_shift;
			} else {
				printf("Invalid seat assignment character %c\n", line[i]);
				return 1;
			}
			
			curr_shift = curr_shift >> 1;
		}

		seats[row_index] |= curr_seat;
	}

	printf("Highest seat id taken on the flight: %d\n", max_seat_id(seats));
	printf("Your seat id is: %d\n", find_seat_id(seats));
	fclose(fd);

	return 0;
}
