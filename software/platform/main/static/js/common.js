function serialize(form)
{
	return Array
		.from(new FormData(form).entries())
		.reduce((m, [k,v]) => Object.assign(m, {[k]:v}), {});
}

function serialize_s(form)
{
	return JSON.stringify(serialize(form));
}
