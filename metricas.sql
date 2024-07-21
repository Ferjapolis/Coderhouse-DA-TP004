Tendencia = divide(COUNTROWS(Calendario),COUNTROWS(DISTINCT(Registros[fecha])))

Media acumulada de Recuento de nominador = 
IF(
	ISFILTERED('Calendario'[Date]),
	ERROR("La medida rápida de inteligencia de tiempo solo se puede agrupar o filtrar mediante la jerarquía de datos proporcionada por Power BI o por la columna de datos principal."),
	VAR __LAST_DATE = ENDOFQUARTER('Calendario'[Date].[Date])
	VAR __DATE_PERIOD =
		DATESBETWEEN(
			'Calendario'[Date].[Date],
			STARTOFQUARTER(DATEADD(__LAST_DATE, -1, QUARTER)),
			ENDOFQUARTER(DATEADD(__LAST_DATE, 1, QUARTER))
		)
	RETURN
		AVERAGEX(
			CALCULATETABLE(
				SUMMARIZE(
					VALUES('Calendario'),
					'Calendario'[Date].[Año],
					'Calendario'[Date].[NroTrimestre],
					'Calendario'[Date].[Trimestre]
				),
				__DATE_PERIOD
			),
			CALCULATE(
				COUNTA('Registros'[nominador]),
				ALL(
					'Calendario'[Date].[NroMes],
					'Calendario'[Date].[Mes],
					'Calendario'[Date].[Día]
				)
			)
		)
)

Usabilidad = DIVIDE( CALCULATE(COUNTROWS(Registros), Registros[nominado]=Registros[nominador]), COUNTROWS(Registros)) * 100

Diferencia porcentual entre Recuento de nominador y 2022 = 
VAR __BASELINE_VALUE = CALCULATE(COUNTA('Registros'[nominador]), 'Calendario'[Year] IN { 2022 })
VAR __MEASURE_VALUE = COUNTA('Registros'[nominador])
RETURN
	IF(
		NOT ISBLANK(__MEASURE_VALUE),
		DIVIDE(__MEASURE_VALUE - __BASELINE_VALUE, __BASELINE_VALUE)
	)

diffExterno = 
CALCULATE(
    COUNTROWS(Registros),
    FILTER(
        'Empresas (2)',
        'Empresas (2)'[Externo] = "Externo"
    )
) - CALCULATE(
    COUNTROWS(Registros),
    FILTER(
        'Empresas (2)',
        'Empresas (2)'[Externo] = "Local"
    )
)