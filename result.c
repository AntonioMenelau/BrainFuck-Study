#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static uint8_t read() {
	int temp = getchar();
	return (uint8_t)(temp != EOF ? temp : 0);
}

int main(void) {
	uint8_t mem[1000000] = {0};
	uint8_t *p = &mem[1000];
	
	p[0] = read();
	while (*p != 0) {
		p[1] = read();
		p++;
	}
	p--;
	while (*p != 0) {
		p--;
	}
	p++;
	while (*p != 0) {
		putchar(p[0]);
		p++;
	}
	
	return EXIT_SUCCESS;
}
