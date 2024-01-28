#pragma once

class Sr74hc595
{
private:
	uint8_t ser;
	uint8_t rclk;
	uint8_t srclk;
	uint8_t state;
public:
	/* Define the pins of a 74HC595 shift register and set its initial state. */
	Sr74hc595(uint8_t ser, uint8_t rclk, uint8_t srclk, uint8_t state)
	{
		this->ser   = ser;
		this->rclk  = rclk;
		this->srclk = srclk;

		pinMode(ser  , OUTPUT);
		pinMode(rclk , OUTPUT);
		pinMode(srclk, OUTPUT);

		sr_write(state);
	}

	/* Write a value to the shift register and latch it out. */
	void sr_write(uint8_t value)
	{
		digitalWrite(rclk, LOW);
		shiftOut(ser, srclk, MSBFIRST, value);
		digitalWrite(rclk, HIGH);
		this->state = value;
	}

	/* Write to index i (i=0 => QA, ...) the value n (n=0 => 0, n>0 => 1). */
	void sr_write_bit(uint8_t i, uint8_t n)
	{
		uint8_t value = state;

		if (n == 0)
			value &= ~(1 << i);
		else
			value |= (1 << i);

		sr_write(value);
	}

	/* Getters. */
	uint8_t get_ser()   { return ser;   }
	uint8_t get_rclk()  { return rclk;  }
	uint8_t get_srclk() { return srclk; }
	uint8_t get_state() { return state; }
};
