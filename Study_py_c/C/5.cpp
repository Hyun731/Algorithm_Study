#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
    int h,w,n,num,m;
    int cnt = 0;
    scanf("%d %d",&h,&w);
    int room[h][w];
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
            room[i][j] = 0;
        
    }
    for (int i = 0; i < w; i++)
    {
        scanf("%d",&n);
        if(n != 0){
            for (int j = h -1; j >= (h - n); j--)
            room[j][i] = 1;
        }
        
    }
    for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                if(room[i][j] == 1){
                    m = j;
                    num = j + 1;
                    while(room[i][num] != 1 && num < w){
                        if(room[i][num] == 0){
                            num++;
                        }
                        else{
                            break;
                        }
                    }
                    if (num < w && num != m + 1) {  // num이 w를 벗어나지 않도록 조건 수정
                        for (int k = m + 1; k < num; k++) {
                            room[i][k] = 2;
                        }
                    }
                }
        }
            num = 0;
    }
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++){
            if(room[i][j] == 2)
                cnt++;
        }
    }
    printf("%d",cnt);
}