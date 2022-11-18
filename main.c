/*
	1 - Teste este programa. Ele espera que o usuário
	digite uma string e tecle "Enter". Então ele retorna
	a string ao usuário.
	2 - Modifique este programa para, em conjunto com 
	códigos anteriores, redirecionar a contagem (progressiva, regressiva).
*/

#include <stdio.h>
#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

void app_main(void)
{
  int i=0;
  char c = 0;
  char str[100];
  memset(str, 0, sizeof(str));
  printf("Digite \"progressiva\" para contar de 1 a 10 e \"regressiva\" para contar de 10 a 1! \n");
  while (c != '\n')
  {
    c = getchar();
    if (c != 0xff)
    {
      str[strlen(str)] = c;
      printf("%c", c);
      
    }
    vTaskDelay(100 / portTICK_PERIOD_MS);
  }

  printf("you typed: %s\n", str);
  printf("DEBUG:ProgTrue: %d\n", strcmp(str,"progressiva\n"));
  printf("DEBUG:RegrTrue: %d\n", strcmp(str,"regressiva\n"));

  if((strcmp(str,"progressiva\n"))==0){
    while(i<10){
        printf("i = %d \n", i);
        i++;
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
  }
  else if(strcmp(str,"regressiva\n")==0){
    while(i<10){
        printf("i = %d \n", 10-i);
        i++;
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
  }
}