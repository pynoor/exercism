def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) == len(strand_b) :
            for x in range(len(strand_a)) :
                if strand_a[x] != strand_b[x] :
                    print (strand_a[x])
                    count = count + 1
                else :
                    count = count
            return (count)
    else :
        return (ValueError)
    
# py.test returns 
# def test_disallow_second_strand_longer(self):
#       with self.assertRaises(ValueError):
#E           AssertionError: ValueError not raised

        
