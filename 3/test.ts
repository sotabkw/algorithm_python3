const DivisorSum = (num: number) => {
  const results = []
  for (let i = 1; i <= num; i++) {
    if (num % i == 0 && i < 2000000) {
      results.push(i)
    }
  }
  return results.reduce(function (sum, element) {
    return sum + element
  }, 0)
}
