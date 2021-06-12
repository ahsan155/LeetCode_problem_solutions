
public class reverse_integer {
	public static int reverse(int x) {
		// if x is negative
		if (x < 0) {
			String num = String.valueOf(x);
			String reversedNumber = "";
			int length = num.length();
			int len = num.length() - 1;
			reversedNumber += "-";
			int counter = 1;
			while (counter < length) {
				reversedNumber += num.charAt(len);
				len--;
				counter++;
			}

			try {
				// System.out.println(reversedNumber);
				int s = Integer.parseInt(reversedNumber);

				if (s < (-2e31)) {
					return 0;
				} else {
					return s;
				}

			} catch (Exception e) {

			}

			// if x is positive
		} else {

			String num = String.valueOf(x);
			String reversedNumber = "";
			int length = num.length();
			int len = num.length() - 1;
			int counter = 0;
			while (counter < length) {
				reversedNumber += num.charAt(len);
				len--;
				counter++;
			}

			try {
				// System.out.println(reversedNumber);
				int s = Integer.parseInt(reversedNumber);

				if (s > ((2e31) - 1)) {
					return 0;
				} else {
					return s;
				}

			} catch (Exception e) {

			}

		}
		return 0;

	}
}
