import java.util.*;
class A{
    static int Calculator(int n1 ,int n2,String c){
        if(c.equals("Addition")){
            return n1+n2;
        }else if(c.equals("Subtraction")){
            return n1-n2;
        }else if(c.equals("Division")){
            return n1/n2;
        }else {
          return n1 * n2;
        }
    }
   public static void main(String args[]){
   Scanner scanner = new Scanner(System.in);
   System.out.println("Enter the number :");
   int n1 = scanner.nextInt();
   System.out.println("Enter number2: ");
   int n2 =scanner.nextInt();
   System.out.println("1.Addition: \n 2.Subtraction: \n 3.Division: \n 4.Multiplication: "
   );
   int option =scanner.nextInt();
   int result=0;
   switch(option){
       case 1:
        result = Calculator(n1,n2,"Addition");
           break;
       case 2:
           result=Calculator(n1,n2,"Subtraction");
           break;
       case 3:
           result=Calculator(n1,n2,"Division");
           break;
       case 4:
           result=Calculator(n1,n2,"");
           break;
        default:
        System.out.print("Did'nt match the Condition !");
   }
   System.out.println(result);
}
}