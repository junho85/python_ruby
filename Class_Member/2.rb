class Cs
  def Cs.class_method()
    p "Class method"
  end
  def instance_method()
    p "Instance method"
  end
end
i = Cs.new()
Cs.class_method() # Class method
i.instance_method() # Instance method
#Cs.instance_method() 오류발생
#i.class_method() 오류발생
