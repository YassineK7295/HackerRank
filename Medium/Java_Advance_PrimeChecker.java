class Prime
{
    public void checkPrime(int... list)
    {
        for (int i:list)
        {
            if (isPrime(i))
            {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
    
    public boolean isPrime(int num)
    {
        if (num == 0 || num == 1)
            return false;
        if (num == 2)
            return true;
        if (num%2 == 0)
            return false;
        for (int i = 3; i < num; i = i + 2)
        {
            if (num%i == 0)
            {
                return false;
            }
        }
        return true;
    }
}
