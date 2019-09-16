#!/usr/bin/ruby
require "set"


class FuzzyPoint
    @@no_of_points = 0
    attr_reader :val
    attr_reader :mem_val
    def initialize(val, mem_val)
        @val = val
        @mem_val = mem_val  # value of membership function
        @@no_of_points += 1
        puts @@no_of_points.to_s
    end
end

class FuzzySet < Set
    def initialize(Points)
    end 
end

FuzzyPoint.new(2, 3)
a = FuzzyPoint.new(2, 3)
p a.val
