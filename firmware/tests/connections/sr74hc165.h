#pragma once

#include "sr74hc595.h"

class Sr74hc165
{
private:
	Sr74hc595 *selector;
	uint8_t cp;
	uint8_t q7;
	uint8_t ce;
	uint8_t pl;

public:
	/* Define the pins of a 74HC165 shift register. selector is the auxiliary
	 * shift register that handles CE and PL, and ce,pl params refer to output
	 * pins on the selector where 0 => QA,...
	 */
	Sr74hc165(Sr74hc595 *selector, uint8_t cp, uint8_t q7, uint8_t ce, uint8_t pl)
	{
		this->selector = selector;
		this->cp = cp;
		this->q7 = q7;
		this->ce = ce;
		this->pl = pl;

		pinMode(cp, OUTPUT);
		pinMode(q7, INPUT );
	}

	/* Read the 74HC165's values. */
	uint8_t sr_read()
	{
		uint8_t data = 0;

		selector->sr_write_bit(pl, 0);
		selector->sr_write_bit(pl, 1);
		selector->sr_write_bit(ce, 0);
		digitalWrite(cp, 0);

		/* Manual shift in. */
		for (uint8_t i = 0; i < 8; i++)
		{
			data |= digitalRead(q7) << i;
			digitalWrite(cp, 1);
			digitalWrite(cp, 0);
		}
		selector->sr_write_bit(ce, 1);

		return data;
	}

	/* Getters. */
	uint8_t get_cp() { return cp; }
	uint8_t get_q7() { return q7; }
	uint8_t get_ce() { return ce; }
	uint8_t get_pl() { return pl; }
};
