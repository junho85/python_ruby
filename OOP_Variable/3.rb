class Cal
  attr_reader :v1, :v2
  attr_writer :v1
  def initialize(v1,v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    return @v1+@v2
  end
  def subtract()
    return @v1-@v2
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def getV1()
    return @v1
  end
end

c1 = Cal.new(10,10)
p c1.add() # 20
p c1.subtract() # 0

c1.setV1('one') # do nothing
p c1.getV1() # 10

c1.setV1(30)
p c1.add() # 40
p c1.getV1() # 30

c1.v1 = 20
p c1.add() # 30
p c1.getV1() # 20
