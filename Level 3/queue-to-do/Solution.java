class Solution {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        System.out.println("Checksum       >> " + solution(17, 40000));
        System.out.println("Execution time >> " + (System.currentTimeMillis() - startTime) + " milliseconds");
    }

    public static int solution(int start, int length) {
        int checksum = 0;

        for (int row = 0; row < length; row ++, start += length) {   // Iterates through every row, shifting the start by the length each time.
            for (int i = start; i < start + length - row; i++) {     // Iterates through every number in the row, ignoring "row" numbers at the end.
                checksum ^= i;
            }
        }
        
        return checksum;
    }
}