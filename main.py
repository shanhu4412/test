student_scores=[78, 79, 67,89, 99]
print(len(student_scores))
print(sum(student_scores))

count=0
total_score=0
max=student_scores[0]
min=student_scores[0]
for ss in student_scores:
  count += 1
  total_score += ss
  if max<ss:
    max=ss
  if min > ss:
    min = ss
print(f'min = {min}')
print(f'max = {max}')
print(f'total count = {count}')
print(f'total score = {total_score}')
avg=total_score/count
print('average = %.02f' % avg)
print('average = {0:.2f}'.format(avg))
print('average = {round(avg,2)}')
