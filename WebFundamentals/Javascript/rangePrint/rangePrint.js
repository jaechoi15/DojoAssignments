//Create a function that can take a start point, end point, and skip amount, to print all numbers in the range.

function printRange(a,b,c)
{
    var start = a;
    var end = b;
    var skip = c;
    
    for (var i = start; i < end; i = skip + i)
    {
        console.log(i);
    }
    
}

printRange(-2,10,3);