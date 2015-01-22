#######
Example
#######
Here are some examples of how to use LNcommon.

MCP23S17
========

::

    >>> import LNcommon.mcp23s17
    >>> mcp =LNcommon.mcp23s17.MCP23S17()
    >>> mcp.gpioa.value = 0xAA
    >>> mcp.gpioa.value
    170
    >>> mcp.gpioa.bits[3].value
    1
