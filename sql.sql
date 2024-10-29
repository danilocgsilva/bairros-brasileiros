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
	historico_buscas hb ON hc.historico_buscas_id = hb.id
GROUP BY hc.historico_buscas_id;

------

SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id),
	hb.id
FROM
	historico_buscas hb
LEFT JOIN
	historico_capturas hc ON  hc.historico_buscas_id = hb.id
GROUP BY hc.historico_buscas_id
;


SELECT
	hb.id as historico_busca_id,
	hb.receita_id,
	COUNT(hc.id)
	-- ,hc.id as historico_captura_id
	-- ,hc.data_captura
	-- ,hc.sucesso
FROM historico_buscas hb
LEFT JOIN
	historico_capturas hc ON hc.historico_buscas_id = hb.id
GROUP BY hc.id
;


SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id)
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON hc.historico_buscas_id = hb.id
GROUP BY hc.historico_buscas_id;


SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id)
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON hc.historico_buscas_id = hb.id
GROUP BY hc.historico_buscas_id;


SELECT
	hc.historico_buscas_id,
	MAX(hc.data_captura)
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON hc.historico_buscas_id = hb.id
GROUP BY hc.historico_buscas_id;


SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id)
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON hc.historico_buscas_id = hb.id
    ,
LATERAL (
	SELECT
    	MAX(hcdl.data_captura)
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
) lateral_data_inicio
GROUP BY hc.historico_buscas_id;



SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id)
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON hc.historico_buscas_id = hb.id
    ,
LATERAL (
	SELECT
    	MAX(hcdl.data_captura) as max_data_captura
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
) lateral_data_inicio
GROUP BY hc.historico_buscas_id;


SELECT
	hc.historico_buscas_id,
	COUNT(hc.historico_buscas_id),
    lateral_data_inicio.max_data_captura,
    lateral_data_fim.min_data_captura
FROM
	historico_capturas hc
LEFT JOIN
	historico_buscas hb ON hc.historico_buscas_id = hb.id
    ,
LATERAL (
	SELECT
    	MAX(hcdl.data_captura) as max_data_captura
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
) lateral_data_inicio
,
LATERAL (
	SELECT
    	MIN(hcdl.data_captura) as min_data_captura
    FROM
    	historico_capturas hcdl
    WHERE
    	hcdl.historico_buscas_id = hc.historico_buscas_id
) lateral_data_fim
GROUP BY hc.historico_buscas_id, lateral_data_inicio.max_data_captura, lateral_data_fim.min_data_captura;


