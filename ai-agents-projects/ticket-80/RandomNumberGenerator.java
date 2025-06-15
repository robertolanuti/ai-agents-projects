import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class RandomNumberGenerator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int number = -1;
        boolean validInput = false;

        while (!validInput) {
            try {
                System.out.print("Please enter a number: ");
                number = scanner.nextInt();
                if (number < 0) {
                    System.out.println("Please enter a non-negative number.");
                } else {
                    validInput = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid integer.");
                scanner.next(); // clear invalid input
            }
        }

        int randomNumber = random.nextInt(number + 1);
        System.out.printf("Random number between 0 and %d (inclusive) is: %d%n", number, randomNumber);
        scanner.close();
    }
}
