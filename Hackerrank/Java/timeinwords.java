import java.util.*;
class time{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String hr=sc.next();
		String min=sc.next();
		Map<String,String> map=new HashMap<String,String>();
		int i=0;
		//for(i=1;i<=29;i++)
		//map.put(Integer.toString(i),(Integer.toString(i)+""));
		map.put("1","one");
		map.put("2","two");
		map.put("3","three");
		map.put("4","four");
		map.put("5","five");
		map.put("6","six");
		map.put("7","seven");
		map.put("8","eight");
		map.put("9","nine");
		map.put("01","one");
		map.put("02","two");
		map.put("03","three");
		map.put("04","four");
		map.put("05","five");
		map.put("06","six");
		map.put("07","seven");
		map.put("08","eight");
		map.put("09","nine");
		map.put("10","ten");
		map.put("11","eleven");
		map.put("12","twelve");
		map.put("13","thirteen");
		map.put("14","fourteen");
		map.put("15","quarter");
		map.put("16","sixteen");
		map.put("17","seventeen");
		map.put("18","eighteen");
		map.put("19","nineteen");
		map.put("20","twenty");
		map.put("21","twenty one");
		map.put("22","twenty two");
		map.put("23","twenty three");
		map.put("24","twenty four");
		map.put("25","twenty five");
		map.put("26","twenty six");
		map.put("27","twenty seven");
		map.put("28","twenty eight");
		map.put("29","twenty nine");
		map.put("30","half");
		
		for(i=1;i<=29;i++)
		{
		if(i==15)
		map.put(Integer.toString(i+30),"quarter");
		else	
		map.put(Integer.toString(i+30),(map.get(Integer.toString(30-i))));	
	    }

	    if(Integer.parseInt(min)==00)
	    	System.out.println(map.get(hr)+" o' clock");
	    else if(Integer.parseInt(min)>=10 ){
	    	if(Integer.parseInt(min)==45)
	    	{
	    	if(Integer.parseInt(hr)<12)
	    	{
	    	if(Integer.parseInt(min)<30)
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	else if(Integer.parseInt(min)>30)
	    	System.out.println(map.get(min)+" to "+map.get(Integer.toString(Integer.parseInt(hr)+1)));	
	    	else if(Integer.parseInt(min)==30)
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    	else if (Integer.parseInt(hr)==12)
	    	{
	    	if(Integer.parseInt(min)<30)
	    	System.out.println(map.get(min)+" minutes past "+map.get(hr));	
	    	else if(Integer.parseInt(min)>30)
	    	System.out.println(map.get(min)+" to "+map.get(Integer.toString(12+1)));	
	    	else if(Integer.parseInt(min)==30)
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    	}
	    	else{
	    	if(Integer.parseInt(hr)<12)
	    	{
	    	if(Integer.parseInt(min)==15)
	    	{
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}	
	    	else if(Integer.parseInt(min)<30)
	    	System.out.println(map.get(min)+" minutes past "+map.get(hr));	
	    	else if(Integer.parseInt(min)>30)
	    	System.out.println(map.get(min)+" minutes to "+map.get(Integer.toString(Integer.parseInt(hr)+1)));	
	    	else if(Integer.parseInt(min)==30)
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    	else if (Integer.parseInt(hr)==12)
	    	{
	    		if(Integer.parseInt(min)==15)
	    	{
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    	else if(Integer.parseInt(min)<30)
	    	System.out.println(map.get(min)+" minutes past "+map.get(hr));	
	    	else if(Integer.parseInt(min)>30)
	    	System.out.println(map.get(min)+" minutes to "+map.get(Integer.toString(12+1)));	
	    	else if(Integer.parseInt(min)==30)
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	        }
	    }
	    else if(Integer.parseInt(min)<10)
	    {
	    	if(Integer.parseInt(hr)<12)
	    	{
	    	if(Integer.parseInt(min)==15)
	    	{
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    		
	    	else if(Integer.parseInt(min)<30)
	    	System.out.println(map.get(min)+" minute past "+map.get(hr));	
	    	else if(Integer.parseInt(min)>30)
	    	System.out.println(map.get(min)+" minute to "+map.get(Integer.toString(Integer.parseInt(hr)+1)));	
	    	else if(Integer.parseInt(min)==30)
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    	else if(Integer.parseInt(hr)==12)
	    	{
	    		if(Integer.parseInt(min)==15)
	    	{
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    	else if(Integer.parseInt(min)<30)
	    	System.out.println(map.get(min)+" minutes past "+map.get(hr));	
	    	else if(Integer.parseInt(min)>30)
	    	System.out.println(map.get(min)+" minutes to "+map.get(Integer.toString(12+1)));	
	    	else if(Integer.parseInt(min)==30)
	    	System.out.println(map.get(min)+" past "+map.get(hr));	
	    	}
	    }

	    }
	}