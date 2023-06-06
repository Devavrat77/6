#include <iostream>;
using namespace std;
class Node
{
public:
char val;
Node *left, *right;
Node()
{
this-&gt;left = NULL;
this-&gt;right = NULL;
}
Node(char val)
{
this-&gt;val = val;
this-&gt;left = NULL;
this-&gt;right = NULL;
}
};
class ExpressionTree
{
private:
Stack *top;
public:
ExpressionTree()
{
top = NULL;
}
void push(Node *temp)
{
if (top == NULL)

top = new Stack(temp);
else
{
Stack *ntemp = new Stack(temp);
ntemp-&gt;next = top;
top = ntemp;
}
}
Node *pop()
{
Node *ptr = top-&gt;node;
top = top-&gt;next;
return ptr;
}
Node *peek()
{
return top-&gt;node;
}
void insert(char val)
{
if (isOperand(val))
{
Node *nptr = new Node(val);
push(nptr);
}
else if (isOperator(val))
{
Node *nptr = new Node(val);
nptr-&gt;left = pop();
nptr-&gt;right = pop();
push(nptr);
}
}
bool isOperand(char ch)
{
return ch;
}
bool isOperator(char ch)
{
return ch ;
}
void construct(string eqn)

{
for (int i = eqn.length() - 1; i &gt;= 0; i--)
insert(eqn[i]);
}
void inOrder(Node *ptr)
{
if (ptr != NULL)
{
inOrder(ptr-&gt;left);
cout&lt;&lt;ptr-&gt;val;
inOrder(ptr-&gt;right);
}
}
};
int main()
{
string exp;
ExpressionTree et;
cout&lt;&lt;&quot;Enter expression in Prefix form: &quot;;
cin&gt;&gt;exp;
et.construct(exp);
cout&lt;&lt;&quot;In-order Traversal of Expression Tree : &quot;;
et.inOrder(et.peek());
return 0;
}