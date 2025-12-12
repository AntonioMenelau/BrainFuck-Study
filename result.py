import sys

mem = [0] * 1000000
i = 1000

mem[i] = (mem[i] + 10) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 10) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 4) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 253) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 7) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 3) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 3) & 0xFF
mem[i + 2] = (mem[i + 2] + mem[i] * 10) & 0xFF
mem[i] = 0
mem[i + 2] = (mem[i + 2] + 2) & 0xFF
sys.stdout.write(chr(mem[i + 2]))
mem[i + 1] = (mem[i + 1] + 8) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 248) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 3) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 250) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 248) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
i += 1
