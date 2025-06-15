import java.util.Random;

public class RandomNumberGenerator {
    public static void main(String[] args) {
        Random random = new Random();
        int num1 = random.nextInt(101);
        int num2 = random.nextInt(101);
        int num3 = random.nextInt(101);

        System.out.println("Generated Numbers: " + num1 + ", " + num2 + ", " + num3);
    }
}