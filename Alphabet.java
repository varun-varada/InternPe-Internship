import java.util.Scanner;

public class Alphabet {
    static void  CheckTypeWriter(char c1){
        if(Character.isLetter(c1)){
           System.out.print("Given Input is a Letter or alphabet");
        //    12@
        }else if(Character.isDigit(c1)){
            System.out.print("Given Input is Digit");
        }else{
            System.out.print("Given Input is Special Character");
        }
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        char c =sc.next().charAt(0);
        CheckTypeWriter(c);
        // System.out.print(c);
    }
}
