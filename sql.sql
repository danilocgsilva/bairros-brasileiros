SELECT
	hb.id,
	hb.receita_id,
	hc.id as historico_captura_id
FROM historico_buscas hb
LEFT JOIN
	historico_capturas hc ON hc.historico_buscas_id = hb.id;

SELECT
	id,
	data_captura,
	sucesso,
	historico_buscas_id
FROM
	historico_capturas;


SELECT
	historico_buscas_id,
	COUNT(historico_buscas_id)
FROM
	historico_capturas
GROUP BY historico_buscas_id;


SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id)
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON  hc.historico_buscas_id = hb.id
GROUP BY hc.historico_buscas_id;


SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id),
	hb.id
FROM
	historico_buscas hb
LEFT JOIN
	historico_capturas hc ON  hc.historico_buscas_id = hb.id
GROUP BY hc.historico_buscas_id;


SELECT
	hb.id as historico_busca_id,
	hb.receita_id,
	COUNT(hc.id)
	-- ,hc.id as historico_captura_id,
	-- hc.data_captura,
	-- hc.sucesso
FROM historico_buscas hb
LEFT JOIN
	historico_capturas hc ON hc.historico_buscas_id = hb.id
GROUP BY hc.id
;

