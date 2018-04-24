import java.util.*;

class sherlock
{
	public static void main(String[] args) {
			int i=0,j=0,a=0,b=0;
			String str="";
			int arr[]=new int[100];
			Scanner sc=new Scanner(System.in);
			int n=sc.nextInt();

					if (n<=1 || n==2 || n==4 || n==7) {
						System.out.println("-1");
					}

					else  {
						loop:
							if (n%3==0) {
								for (i=0;i<n ;i++){
									str+="5";
								}	
							}

						    else if (n%5==0) {
								for (i=0;i<n ;i++){
									str+="3";
								}	
							}

							else if (n%3==0 && n%5==0) {
								for (i=0;i<n ;i++){
									str+="5";
								}	
							}	

							else{
								for (a=0;a<n ;a++ ) {
									for (b=0;b<n ;b++ ) {
											if((a+b)==n && ((a%3==0 && b%5==0) || (a%5==0 && b%3==0))){
												//System.out.println(a+" "+b);
												break loop; 
											}	

									}		
								}
							}
					    if (a%3==0 && b%5==0) {
													for (i=0;i<a;i++)
													str+="5";
													for (i=0;i<b ;i++)
													str+="3";				
												}

												else if(a%5==0 && b%3==0)
														{
															for (i=0;i<b ;i++)
															str+="5";     
															for (i=0;i<a;i++)
															str+="3";
														}
					System.out.println(str);
					}		
					//else if(n<=1){
						
				//	}	
							
					 		
			}
							

	}