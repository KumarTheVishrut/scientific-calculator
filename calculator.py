import math
import logging
import os

# Configure logging for ELK monitoring
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler(f"{log_dir}/calculator.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def square_root(x):
    """Compute square root of x. x must be >= 0."""
    if x < 0:
        raise ValueError(f"Cannot compute square root of negative number: {x}")
    result = math.sqrt(x)
    logger.info(f"square_root({x}) = {result}")
    return result


def factorial(x):
    """Compute factorial of x. x must be a non-negative integer."""
    if not isinstance(x, int) or x < 0:
        raise ValueError(f"Factorial requires a non-negative integer, got: {x}")
    result = math.factorial(x)
    logger.info(f"factorial({x}) = {result}")
    return result


def natural_log(x):
    """Compute natural logarithm (base e) of x. x must be > 0."""
    if x <= 0:
        raise ValueError(f"Logarithm undefined for non-positive values: {x}")
    result = math.log(x)
    logger.info(f"natural_log({x}) = {result}")
    return result


def power(x, b):
    """Compute x raised to the power b."""
    result = math.pow(x, b)
    logger.info(f"power({x}, {b}) = {result}")
    return result


def display_menu():
    print("\n" + "="*45)
    print("      Scientific Calculator - CS816")
    print("="*45)
    print("  1. Square Root  √x")
    print("  2. Factorial    x!")
    print("  3. Natural Log  ln(x)")
    print("  4. Power        x^b")
    print("  5. Exit")
    print("="*45)


def main():
    logger.info("Scientific Calculator started")
    print("\nWelcome to the Scientific Calculator!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == '1':
                x = float(input("Enter x: "))
                print(f"  √{x} = {square_root(x)}")

            elif choice == '2':
                x = int(input("Enter x (non-negative integer): "))
                print(f"  {x}! = {factorial(x)}")

            elif choice == '3':
                x = float(input("Enter x (x > 0): "))
                print(f"  ln({x}) = {natural_log(x)}")

            elif choice == '4':
                x = float(input("Enter base x: "))
                b = float(input("Enter exponent b: "))
                print(f"  {x}^{b} = {power(x, b)}")

            elif choice == '5':
                logger.info("Scientific Calculator exited by user")
                print("Goodbye!")
                break

            else:
                print("  Invalid choice. Please enter 1-5.")
                logger.warning(f"Invalid menu choice: {choice}")

        except ValueError as e:
            print(f"  Error: {e}")
            logger.error(f"ValueError: {e}")
        except Exception as e:
            print(f"  Unexpected error: {e}")
            logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
