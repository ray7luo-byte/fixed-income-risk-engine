import bisect
class Curve:
    def __init__(self,tenors,rates):
        self.tenors=tenors
        self.rates=rates

    @classmethod
    def from_dict(cls,d):
        items=sorted(d.items())
        return cls([t for t, _ in items],[r for _,r in items])

    def rate(self,t):
        if t <= self.tenors[0]:
            return self.rates[0]
        if t >= self.tenors[-1]:
            return self.rates[-1]
        i= bisect.bisect_right(self.tenors,t)-1
        t1,t2=self.tenors[i],self.tenors[i+1]
        r1,r2=self.rates[i],self.rates[i+1]
        return r1+(r2-r1)*(t-t1)/(t2-t1)
    
    def df(self,t):
        from fire.pricing import discount_factor
        return discount_factor(self.rate(t),t,"semi")
