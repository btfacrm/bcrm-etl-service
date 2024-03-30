%dw 2.0
output json
---
if (payload != null)
	payload map (item, value) ->
	{
		id: item.Id,
	    firstName: item.FirstName default '',
	    lastName: item.LastName default '',
	    email: item.Email default ''
	}
else {}