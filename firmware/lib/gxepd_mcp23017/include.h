/* This is a fork of J-M Zingg's GxEPD library.
 * See: https://github.com/ZinggJM/GxEPD
 *
 * This fork is mostly the same except for that some pins are controlled by an
 * MCP23017 using Bertrand Lemasle's MCP23017 library.
 * See: https://github.com/blemasle/arduino-mcp23017
 */

#include <MCP23017.h>  // MCP23017 by Bertrand Lemasle
#include "GxEPD.cpp"
#include "GxIO/GxIO_SPI/GxIO_SPI.cpp"
#include "GxGDEM029T94/GxGDEM029T94.cpp"
