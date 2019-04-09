-------------------------------------------------------------------------------------------
3B to HMI
-------------------------------------------------------------------------------------------
```json
{
	"type"		: 	"info",
	"message"	:	"text",
	"device"	: 	device_number
}
```
```json
{
	"type"		: 	"error",
	"message"	:	"text",
	"device"	: 	device_number
}
```
```json
{
	"type"		: 	"warning",
	"message"	:	"text",
	"device"	: 	device_number
}
```
-------------------------------------------------------------------------------------------
# Sensoren & actuatoren status uitlezen
-------------------------------------------------------------------------------------------
```json
{
	"type"		:	"barrier",
	"state"		: 	0/1										(open = 0, dicht = 1)
}
```
```json
{
	"type"		:	"sos",
	"state"		: 	0/1/2,									(0 = niks, 1 = 1e helft, 2 = 2e helft)
	"data"		: 
					{
						"cause" : "melding" 
						"amount": aantal_wagens_in_tunnel
					}
}
```
```json
{
	"type"		:	"trafficlight",
	"state"		: 	0/1/2/3/4							 		(0 = groen , 1 = geel ,2 = geel knipperen 3= rood, 4=gedoofd)
}
```
```json
{
	"type"		:	"lights",
	"status" 	: 	0/1/2 										(0 = alles uit, 1 = normaal, 2 = alles 100%)
}
```
```json
{
	"type"		:	"cctv",
	"state"		: 	0/1										(0 = 1e helft, 1 = 2e helft)
}
```

-------------------------------------------------------------------------------------------
HMI to 3B
-------------------------------------------------------------------------------------------
```json
{
"type"			: 	"tunnel",
"action" 		: 	0/1/2									(0 = open, 1 = warning, 2 = sluiten)
}
```
```json
{
"type"			: 	"cctv",
"action"		: 	0/1 									(0 = left, 1 = right)
}
```
