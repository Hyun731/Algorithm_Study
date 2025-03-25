#include <stdio.h>
int num[10000] = {0,};

int main() {
  int n,inp;
  scanf("%d",&n);
  for(int i=0;i<n;i++) {
    scanf("%d",&inp);
    num[inp-1]++;
  }
  for(int i=0;i<10000;i++) {
    for(int j=0;j<num[i];j++) {
      printf("%d\n",i+1);
    }
  }
}