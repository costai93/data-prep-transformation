# DATA PREP & TRANSFORMATION | AVALIAÇÃO – CASO DE USO PRÁTICO

Este projeto tem como objetivo preparar e transformar os dados de um conjunto de dados brutos de e-commerce brasileiro para atender a demandas analíticas, utilizando os modelos Star Schema e Wide Table. Uma etapa crucial foi a definição da abordagem de tempestividade para o fluxo de transformação. As opções consideradas foram **Batch**, **Micro-Batch**, e **Fluxo Contínuo (Streaming)**.

## Abordagens Consideradas

### Batch Processing
- **Descrição**: Processa dados em grandes blocos, geralmente em intervalos predefinidos como diariamente ou semanalmente.
- **Vantagens**:
  - Simples de implementar.
  - Menor custo para processar grandes volumes de dados.
- **Desvantagens**:
  - Alta latência, tornando os dados menos atualizados.

**Uso no projeto**: A abordagem de Batch é adequada para a carga inicial dos dados e processamento periódico, mas não atende totalmente à necessidade de atualizações mais frequentes para análises.

---

### Micro-Batch Processing
- **Descrição**: Processa dados em blocos menores em intervalos curtos, como a cada hora ou minutos.
- **Vantagens**:
  - Reduz a latência comparada ao Batch.
  - Requer menos complexidade que Streaming.
- **Desvantagens**:
  - Demanda um esforço moderado de configuração.

**Uso no projeto**: O Micro-Batch foi escolhido como a abordagem principal, pois oferece um equilíbrio ideal entre frequência de atualização e simplicidade de implementação, atendendo ao grão mensal e anual das análises sem a complexidade desnecessária de um fluxo contínuo.

---

### Fluxo Contínuo (Streaming)
- **Descrição**: Processa dados continuamente à medida que são gerados.
- **Vantagens**:
  - Fornece dados quase em tempo real.
  - Ideal para análises em tempo real.
- **Desvantagens**:
  - Alta complexidade e custo operacional.

**Uso no projeto**: Embora o Streaming seja uma abordagem avançada, sua latência mínima não é necessária para o escopo deste projeto, onde os dados são agregados mensalmente e anualmente.

---

## Escolha Final: Micro-Batch
A abordagem **Micro-Batch** foi selecionada pelos seguintes motivos:

1. **Necessidade Analítica**: O objetivo do projeto é transformar os dados em um grão de mês e ano, permitindo uma análise atualizada sem necessidade de latência mínima.
2. **Latência Moderada**: Atualizações regulares (diárias ou horárias) são suficientes para o escopo das análises.
3. **Simplicidade e Eficiência**: Comparado ao Streaming, o Micro-Batch é mais simples de implementar e manter, sem comprometer a tempestividade necessária.

---

## Estratégia de Implementação

### Intervalo de Atualização
- O fluxo será configurado para executar em intervalos curtos, como uma vez a cada hora ou diariamente, dependendo da necessidade analítica.

### Ferramentas
- O fluxo será automatizado com ferramentas como **Python** (para scripts SQL).
- O agendamento do processo de Micro-Batch pode ser configurado utilizando ferramentas como o cron no Linux ou o Task Scheduler no Windows. A seguir, demonstraremos a configuração de um cron job no Linux para executar o processo automaticamente a cada hora:

Abra o editor de agendamentos do cron executando o comando no terminal:
`crontab -e`

Inclua a seguinte linha no arquivo de configuração:
`0 * * * * /caminho/para/o/script.sh >> /caminho/para/o/log.log 2>&1`

### Incremento dos Dados
- Consultas SQL incrementais serão utilizadas para processar apenas os dados novos desde a última execução, otimizando o desempenho e reduzindo o uso de recursos.

