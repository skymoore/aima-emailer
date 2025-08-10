def generate_email_html(
    full_name,
    nationality,
    appointment_date,
    service_location,
    passport_number,
    correct_address,
    contact_number,
    rental_contract_link,
    passport_photo_link,
    temp_id_link,
):
    """
    Generate a formatted HTML email for requesting address update and residence proof.

    Args:
        full_name (str): The full name of the person.
        nationality (str): The nationality (e.g., 'ucraniana').
        appointment_date (str): The approximate appointment date.
        service_location (str): The service location (e.g., 'Loja do Cidadão de …').
        passport_number (str): The passport number.
        correct_address (str): The complete correct address.

    Returns:
        str: The formatted HTML email content.
    """
    html_template = """
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pedido de atualização de morada e envio de comprovativo de residência</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
                color: #333333;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .email-container {
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                border: 1px solid #dddddd;
                border-radius: 5px;
                overflow: hidden;
            }
            .header {
                background-color: #007bff;
                color: #ffffff;
                padding: 20px;
                text-align: center;
            }
            .content {
                padding: 20px;
            }
            .footer {
                background-color: #f4f4f4;
                padding: 10px;
                text-align: center;
                font-size: 12px;
                color: #666666;
            }
            h2 {
                font-size: 18px;
                margin-bottom: 10px;
            }
            ul {
                list-style-type: disc;
                padding-left: 20px;
            }
            .bold {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1 style="margin: 0; font-size: 20px;">Pedido de Atualização de Morada</h1>
            </div>
            <div class="content">
                <p>Exmos. Senhores,</p>
                <p>Venho por este meio informar que realizei a minha marcação na AIMA há mais de 6 meses, mas ainda não recebi o comprovativo nem o título de residência.</p>
                <p>Verifiquei que, infelizmente, a morada foi registada incorretamente, o que pode ter impedido a entrega do meu título.</p>
                <p>Solicito a atualização da morada correta nos vossos registos e o reenvio do comprovativo e do cartão, caso já tenham sido emitidos.</p>
                <h2>Dados do meu processo:</h2>
                <ul>
                    <li><span class="bold">Nome completo:</span> [teu nome]</li>
                    <li><span class="bold">Nacionalidade:</span> [ex: ucraniana]</li>
                    <li><span class="bold">Data da marcação:</span> [data aproximada]</li>
                    <li><span class="bold">Local de atendimento:</span> [por exemplo, Loja do Cidadão de …]</li>
                    <li><span class="bold">Nº de passaporte:</span> [número do passaporte]</li>
                    <li><span class="bold">Contacto:</span> [escreve aqui o teu contacto]</li>
                </ul>
                <h2>Morada correta:</h2>
                <p>[escreve aqui a tua morada atual, completa]</p>
                <p>Em anexo envio cópia do meu passaporte, contrato de arrendamento e o recibo comprovativo de pedido de residência.</p>
                <p><a href="[link para o contrato de arrendamento]">Link para o contrato de arrendamento</a>.</p>
                <p><a href="[link para a foto do passaporte]">Link para a foto do passaporte</a>.</p>
                <p><a href="[link para o recibo comprovativo de pedido de residência]">Link para o recibo comprovativo de pedido de residência</a>.</p>
                <p>Agradeço desde já a atenção e aguardo o vosso retorno com urgência.</p>
                <p>Com os melhores cumprimentos,</p>
                <p>[teu nome]</p>
            </div>
        </div>
    </body>
    </html>
    """

    # Replace placeholders with provided values
    html = html_template.replace("[teu nome]", full_name)
    html = html.replace("[ex: ucraniana]", nationality)
    html = html.replace("[data aproximada]", appointment_date)
    html = html.replace("[por exemplo, Loja do Cidadão de …]", service_location)
    html = html.replace("[número do passaporte]", passport_number)
    html = html.replace("[escreve aqui a tua morada atual, completa]", correct_address)
    html = html.replace("[escreve aqui o teu contacto]", contact_number)
    html = html.replace("[link para o contrato de arrendamento]", rental_contract_link)
    html = html.replace("[link para a foto do passaporte]", passport_photo_link)
    html = html.replace("[link para o recibo comprovativo de pedido de residência]", temp_id_link)
    return html
