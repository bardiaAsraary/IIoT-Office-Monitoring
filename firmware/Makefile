CC = riscv64-unknown-elf-gcc
CFLAGS = -march=rv32imac -mabi=ilp32 -nostartfiles -T link.ld
LDFLAGS = -lssl -lcrypto

SRC = main.c
ELF = firmware.elf

all: $(ELF)

$(ELF): $(SRC)
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)
	
clean:
	rm -f $(ELF)