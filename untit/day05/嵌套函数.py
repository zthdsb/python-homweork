def foo():
    print("this is foo")
    def bar():
        print("that is bar")
    bar()
foo()