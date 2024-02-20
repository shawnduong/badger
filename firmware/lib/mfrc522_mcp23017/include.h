/* This is a fork of Miguel Balboa's rfid library.
 * See: https://github.com/miguelbalboa/rfid
 *
 * This fork is mostly the same except for that SS and RST are controlled by an
 * MCP23017 using Bertrand Lemasle's MCP23017 library.
 * See: https://github.com/blemasle/arduino-mcp23017
 */

#include "../mcp23017_modded/MCP23017.cpp"
#include "MFRC522.cpp"
