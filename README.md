## Aima Emailer

#### Installation
```bash
poetry install
```

#### Example Usage
```bash
aimail \
    --full-name "Your Name" \
    --nationality "Lituanian" \
    --appointment-date "2025-01-01" \
    --service-location "Loja AIMA - Rio Tinto" \
    --passport-number "1234567890" \
    --correct-address "Somewhere in lisbon, 1234-222" \
    --contact-number "+351 123 456 789" \
    --from-email "my-address@example.com" \
    --to-email "aima@aima.gov.pt" \
    --subject "Pedido de Atualização de Morada" \
    --attachment "assets/passport.png" \
    --attachment "assets/aima-temp-id.jpg" \
    --attachment "assets/rental-contract.pdf"
```
