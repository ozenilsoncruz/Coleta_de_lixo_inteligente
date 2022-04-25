# Coleta de lixo inteligente

## Problema 1 - Conectividade e Concorrência
<div align="justify">
  Neste protótipo do sistema, existe um caminhão de lixo que cobre um total de T lixeiras monitoradas. O objetivo é semi-automatizar o serviço público de coleta de lixo, fornecendo assistência aos coletores para melhorar sua eficiência através da priorização das lixeiras mais críticas (próximas de encher).
</div>
  
### Restrições
<div align="justify">
  <ol>
    <li> 
       O sistema deve ser implementado através de um serviço seguindo uma arquitetura de Nuvem IoT centralizada, como apresentado na Figura 1. Nesta arquitetura, os dados gerados pelos sensores nas lixeiras serão transmitidos pela internet até o centro de dados em nuvem;
    </li>
    <li> 
      Os dados das interfaces devem ser obtidos através usando um protocolo baseado em uma API REST:  
      <ol> 
        <li> na interface móvel dos caminhões em campo, um funcionário pode identificar a próxima lixeira a ser coletada e suas informações; </li>
        <li> na interface do escritório, o administrador do sistema pode ver as informações sobre o estado das lixeiras, bloquear ou liberar a abertura da lixeira (colocar lixo), intervir junto ao caminhão sobre a lixeira que deve ser coletada (ordem), e acompanhar a coleta em tempo real; </li>
      </ol>
    </li>
    <li> 
      Para facilitar a avaliação do protótipo, a lixeira (e sensores) será simulada através de um software para geração de dados fictícios. Para emular mais perfeitamente o cenário proposto, cada dispositivo lixeira deve ser um processo executado em um computador em algum lugar na internet;
    </li>
    <li>
      A lixeira virtual deve se comunicar pela rede e possuir uma interface gráfica para definir a geração dos dados em tempo real. Por exemplo, uma caixa de entrada pode definir a capacidade da lixeira e outra com botões pode permitir a sua alteração (adicionar algum lixo);
    </li>
    <li>
      Por questões dos direitos comerciais, NENHUM framework de terceiro deve ser usado para implementar a solução do problema. Neste caso, apenas os mecanismos básicos presentes no sistema operacional podem ser usados para implementar a comunicação sobre uma arquitetura de rede baseada na Internet (TCP/IP).
    </li>
  </ol> 
 </div>
 
 ## Autores
<div align="justify">
  <li><a href="https://github.com/ian-zaque">@ian-zaque</a></li>
  <li><a href="https://github.com/ozenilsoncruz">@ozenilsoncruz</a></li>
</div>

## Máquina
<div align="justify">
  <ol>
    <li> 
       Instalação do python 3.10.4;
     </li>
    <li> 
       Bibliotecas nativas utilizadas:
      <ol> 
        <li>json; </li>
        <li>random; </li>
        <li>select; </li>
        <li>socket; </li>
        <li>string; </li>
        <li>sys; </li>
        <li>threading; </li>
        <li>tkinter; </li>
      </ol>
    </li>
  </ol>
</div>

## Instruções
<div align="justify">
   <ol>
    <li> 
       Executar o Servidor
    </li>
     <li> 
       Executar as Lixeiras
    </li>
     <li> 
       Executar os Caminhoes
    </li>
     <li> 
       Executar o Administrador
    </li>
  </ol> 
</div>
