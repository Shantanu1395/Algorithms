import java.util.*;

class sherlock
{
	public static void main(String[] args) {
			int i=0,j=0,a=0,b=0;
			String str[]=new String[1000];
			int arr[]=new int[100];
			int n[]=new int[100];
			Scanner sc=new Scanner(System.in);
			int t=sc.nextInt();
			for (j=0;j<t;j++ ) {
				n[j]=sc.nextInt();	
			}
				for(j=0;j<t;j++){
					if (n[j]<=1 || n[j]==2 || n[j]==4 || n[j]==7) {
						System.out.println("-1");
					}

					else  {
						loop:
							if (n[j]%3==0) {
								for (i=0;i<n[j] ;i++){
									str[j]+="5";
								}	
							}

						    else if (n[j]%5==0) {
								for (i=0;i<n[j] ;i++){
									str[j]+="3";
								}	
							}

							else if (n[j]%3==0 && n[j]%5==0) {
								for (i=0;i<n[j] ;i++){
									str[j]+="5";
								}	
							}	

							else{
								for (a=0;a<n[j] ;a++ ) {
									for (b=0;b<n[j] ;b++ ) {
											if((a+b)==n[j] && ((a%3==0 && b%5==0) || (a%5==0 && b%3==0))){
												break loop; 
											}	

									}		
								}
							}
					    if (a%3==0 && b%5==0) {
													for (i=0;i<a;i++)
													str[j]+="5";
													for (i=0;i<b ;i++)
													str[j]+="3";				
												}

												else if(a%5==0 && b%3==0)
														{
															for (i=0;i<b ;i++)
															str[j]+="5";     
															for (i=0;i<a;i++)
															str[j]+="3";
														}
					System.out.println(str[j].substring(4));
					}		
					//else if(n<=1){
						
				//	}	
					}		
					 		
			}
							

	}