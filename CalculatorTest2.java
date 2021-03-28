/**
 * @brief Test for Calculator class, testing division by 0
 */
public class CalculatorTest2 {
    public static void main(String[] args){
        Calculator c = new Calculator(3,0);
        System.out.println(c.divide());
    }
}