
public class Solution{
	private TreeNode cur;
	private Stack<TreeNode> stack = new Stack<TreeNode>();
	public Solution(TreeNode root) {
		cur = root;
	}
	public boolean hasNext() {
		return (cur != null || !stack.empty());
	}
	public TreeNode next() {
		while(cur != null) {
            stack.push(cur);
            cur = cur.left;
        }
        TreeNode result = stack.pop();
        cur = result.right;
        return result;
	}

————————————————
版权声明：本文为CSDN博主「u010157717」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u010157717/article/details/41266873