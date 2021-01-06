class Solution:
    def minTimeToVisitAllPoints(points) -> int:
        step = 0
        for i in range(len(points)-1):
            start = points[i]
            end = points[i+1]
            if (start[0]==end[0] and start[1] !=end[1]) or (start[1]==end[1] and start[0]!=end[0]):
                step += max(abs(start[1]-end[1]),abs(start[0]-end[0]))
            elif start[0]!=end[0] and start[1] !=end[1]:
                row = abs(start[1]-end[1])
                col = abs(start[0]-end[0])
                if row<col:
                    step += row
                    step += abs(start[0]-(start[1]-end[1])-end[0])
                else:
                    step += col
                    step += abs(start[1] - (start[0] - end[0]) - end[1])

                # if end[0]-start[0]>0
                # dis = min(end[0]-start[0],end[1]-start[1])
                # step += abs(dis)
                # start[0] += dis
                # start[1] += dis
                # if start[0]==end[0] and start[1] !=end[1]:
                #     step += abs(start[1]-end[1])
                # elif start[1]==end[1] and start[0]!=end[0]:
                #     step += abs(start[0]-end[0])
        return step
if __name__=='__main__':

    s = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
    # s=[[559,511],[932,618]]
    print(Solution.minTimeToVisitAllPoints(s))


