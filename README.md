## Desafio Python - Gerador de Relatório de Vendas Avançado

### Arquitetura
Utilizado uma arquitetura clean architecture, separando a parte da infra do dominio, dessa forma, é possível aproveitar todo o core da aplicação em outros projetos que não são efetivamente cli.

### Comandos


```sh
uv run dev --file='path_to_file' --start='2025-01-31' --end='2026-01-31' --format=json|text
```

## Testes

### Os testes estão divididos em duas suites (unit, e2e)

### Rodar testes unitários
```sh
uv run task test-unit
```

### Rodar testes e2e
```sh
uv run task test-e2e
```

### Rodar coverage
```sh
uv run task test-cov
```

### Build
```sh
uv run task build
```
Após o build é possível rodar o script como desafio-mirante 

```sh
desafio-mirante --file='path_to_file' --format=json
```