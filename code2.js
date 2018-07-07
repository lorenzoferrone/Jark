let quicksort:
	[] => []
	[n] => [n]
	[head, *rest] =>
		let smaller: [x for x in rest if x <= head]
		let bigger: [x for x in rest if x > head]
		return quicksort(smaller) ++ head ++ quicksort(bigger)


let isPrime:
	let smallPrimes = [2, 3, 5, 7, 11]
	n in smallPrimes => true
	0, 1 => false
	n =>
		let testDivisor: [x for x in range(2, sqrt(n))]
		all(n % x == 0 for x in testDivisor)