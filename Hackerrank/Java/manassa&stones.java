/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package javaapplication1;

import java.util.Scanner;

/**
 *
 * @author Administrator
 */
public class JavaApplication1 {
   

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int[][] arr=new int[1000][1000];
        int num[]=new int[1000];
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int i=0,j=0;
        for(i=0;i<n;i++)
        {
            num[i]=sc.nextInt();
            int a=sc.nextInt();
            int b=sc.nextInt();
            
            
            for(j=0;j<=num[i]-1;j++)
            {
                if(b>a)
                arr[i][j]=b*j+a*(num[i]-1-j);
                else if(a>b)
                arr[i][j]=a*j+b*(num[i]-1-j);    
                else if(a==b)
                {
                    arr[i][j]=b*j+a*(num[i]-1-j);
                        break;
                }       
            }
        }
        
        for ( i = 0; i < n; i++) {
            for (j = 0; j <=num[i]-1; j++) {
            if(arr[i][j]>0)    
                System.out.print(arr[i][j]+" ");
            }
            System.out.println("");
        }
        // TODO code application logic here
    }
    
}
