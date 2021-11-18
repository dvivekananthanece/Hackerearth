import java.util.Scanner;

public class AliandHelpingInnocentPeople {
	public static String validOrNot(String aliString) {
		int result =0;
		String vowels ="AEIOUY";
		char[] aliChar = aliString.toCharArray();
		for(int i=0;i<aliString.length();i++) {
			if(i==0||i==3||i==4||i==7) {
				int k =Integer.parseInt(String.valueOf(aliChar[i]));
				int j =Integer.parseInt(String.valueOf(aliChar[i+1]));
				if((k+j)%2==0 && !vowels.contains(Character.toString(aliChar[2]))){					
						result++;					
				}
			}
		}
		if(result == 4) {
			return "valid";
		}
		else {
		return "invalid";
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		String inputString = scanner.nextLine();
		System.out.print(validOrNot(inputString));
		

	}

}
