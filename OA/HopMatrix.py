def funcHopSkipJump(matrix):
	# Write your code here
	row, col = len(matrix), len(matrix[0])
	cur_i,cur_j = 0,0
	cur = -1
	jumped = False

	while True:
		jumped = False
		#Jump down
		for i in range(cur_i,row,2):
			if matrix[i][cur_j] != '#':
				cur = matrix[i][cur_j]
				matrix[i][cur_j] = '#'
				
			cur_i = i
		print(matrix)
		#Jump right
		if jumped:
			jumped = False
			for j in range(cur_j,col,2):
				if matrix[cur_i][j] != '#':
					cur = matrix[cur_i][j]
					matrix[cur_i][j] = '#'
					jumped = True
				cur_j = j
			print(matrix)
		#Jump up
		if jumped:
			jumped = False
			for i in range(cur_i,-1,-2):
				if matrix[i][cur_j] != '#':
					cur = matrix[i][cur_j]
					matrix[i][cur_j] = '#'
					jumped = True
				cur_i = i
			print(matrix)
		#Jump left
		if jumped:
			jumped = False
			for j in range(cur_j,-1,-2):
				if matrix[cur_i][j] != '#':
					cur = matrix[cur_i][j]
					matrix[cur_i][j] = '#'
					jumped = True
				cur_j = j
			print(matrix)
		print(matrix)
		if not jumped:
			
			if 0<=cur_i+1<row and 0<=cur_j-1<col and matrix[cur_i+1][cur_j-1] !='#':
				cur_i += 1
				cur_j -= 1
			elif 0<=cur_i+1<row and 0<=cur_j+1<col and matrix[cur_i+1][cur_j+1] !='#':
				cur_i += 1
				cur_j += 1
			elif 0<=cur_i-1<row and 0<=cur_j+1<col and matrix[cur_i-1][cur_j+1] !='#':
				cur_i -= 1
				cur_j += 1
			elif 0<=cur_i-1<row and 0<=cur_j-1<col and matrix[cur_i-1][cur_j-1] !='#':
				cur_i -= 1
				cur_j -= 1
			else:
				break
		print(matrix)

	return cur

def main():
	#input for matrix
	matrix = [[9,8,7,6],
	   [5,4,3,2],
       [1,10,11,12]]
	matrix_rows,matrix_cols  = 3,4
	
	
	result = funcHopSkipJump(matrix)
	print(result)	

if __name__ == "__main__":
	main()