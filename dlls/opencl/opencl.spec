@ stdcall clBuildProgram(ptr long ptr ptr ptr ptr)
@ stdcall clCompileProgram(ptr long ptr ptr long ptr ptr ptr ptr)
@ stdcall clCreateBuffer(ptr int64 long ptr ptr)
@ stdcall clCreateCommandQueue(ptr ptr int64 ptr)
@ stdcall clCreateContext(ptr long ptr ptr ptr ptr)
@ stdcall clCreateContextFromType(ptr int64 ptr ptr ptr)
@ stdcall clCreateImage(ptr int64 ptr ptr ptr ptr)
@ stdcall clCreateImage2D(ptr int64 ptr long long long ptr ptr)
@ stdcall clCreateImage3D(ptr int64 ptr long long long long long ptr ptr)
@ stdcall clCreateKernel(ptr ptr ptr)
@ stdcall clCreateKernelsInProgram(ptr long ptr ptr)
@ stdcall clCreateProgramWithBinary(ptr long ptr ptr ptr ptr ptr)
@ stdcall clCreateProgramWithBuiltInKernels(ptr long ptr ptr ptr)
@ stdcall clCreateProgramWithSource(ptr long ptr ptr ptr)
@ stdcall clCreateSampler(ptr long long long ptr)
@ stdcall clCreateSubBuffer(ptr int64 long ptr ptr)
@ stdcall clCreateSubDevices(ptr ptr long ptr ptr)
@ stdcall clCreateUserEvent(ptr ptr)
@ stdcall clEnqueueBarrier(ptr)
@ stdcall clEnqueueBarrierWithWaitList(ptr long ptr ptr)
@ stdcall clEnqueueCopyBuffer(ptr ptr ptr long long long long ptr ptr)
@ stdcall clEnqueueCopyBufferRect(ptr ptr ptr ptr ptr ptr long long long long long ptr ptr)
@ stdcall clEnqueueCopyBufferToImage(ptr ptr ptr long ptr ptr long ptr ptr)
@ stdcall clEnqueueCopyImage(ptr ptr ptr ptr ptr ptr long ptr ptr)
@ stdcall clEnqueueCopyImageToBuffer(ptr ptr ptr ptr ptr long long ptr ptr)
@ stdcall clEnqueueFillBuffer(ptr ptr ptr long long long long ptr ptr)
@ stdcall clEnqueueFillImage(ptr ptr ptr ptr ptr long ptr ptr)
@ stdcall clEnqueueMapBuffer(ptr ptr long int64 long long long ptr ptr ptr)
@ stdcall clEnqueueMapImage(ptr ptr long int64 ptr ptr ptr ptr long ptr ptr ptr)
@ stdcall clEnqueueMarker(ptr ptr)
@ stdcall clEnqueueMarkerWithWaitList(ptr long ptr ptr)
@ stdcall clEnqueueMigrateMemObjects(ptr long ptr int64 long ptr ptr)
@ stdcall clEnqueueNDRangeKernel(ptr ptr long ptr ptr ptr long ptr ptr)
@ stdcall clEnqueueNativeKernel(ptr ptr ptr long long ptr ptr long ptr ptr)
@ stdcall clEnqueueReadBuffer(ptr ptr long long long ptr long ptr ptr)
@ stdcall clEnqueueReadBufferRect(ptr ptr long ptr ptr ptr long long long long ptr long ptr ptr)
@ stdcall clEnqueueReadImage(ptr ptr long ptr ptr long long ptr long ptr ptr)
@ stdcall clEnqueueTask(ptr ptr long ptr ptr)
@ stdcall clEnqueueUnmapMemObject(ptr ptr ptr long ptr ptr)
@ stdcall clEnqueueWaitForEvents(ptr long ptr)
@ stdcall clEnqueueWriteBuffer(ptr ptr long long long ptr long ptr ptr)
@ stdcall clEnqueueWriteBufferRect(ptr ptr long ptr ptr ptr long long long long ptr long ptr ptr)
@ stdcall clEnqueueWriteImage(ptr ptr long ptr ptr long long ptr long ptr ptr)
@ stdcall clFinish(ptr)
@ stdcall clFlush(ptr)
@ stdcall clGetCommandQueueInfo(ptr long long ptr ptr)
@ stdcall clGetContextInfo(ptr long long ptr ptr)
@ stdcall clGetDeviceIDs(ptr int64 long ptr ptr)
@ stdcall clGetDeviceInfo(ptr long long ptr ptr)
@ stdcall clGetEventInfo(ptr long long ptr ptr)
@ stdcall clGetEventProfilingInfo(ptr long long ptr ptr)
@ stdcall clGetExtensionFunctionAddress(ptr)
@ stdcall clGetExtensionFunctionAddressForPlatform(ptr ptr)
@ stdcall clGetImageInfo(ptr long long ptr ptr)
@ stdcall clGetKernelArgInfo(ptr long long long ptr ptr)
@ stdcall clGetKernelInfo(ptr long long ptr ptr)
@ stdcall clGetKernelWorkGroupInfo(ptr ptr long long ptr ptr)
@ stdcall clGetMemObjectInfo(ptr long long ptr ptr)
@ stdcall clGetPlatformIDs(long ptr ptr)
@ stdcall clGetPlatformInfo(ptr long long ptr ptr)
@ stdcall clGetProgramBuildInfo(ptr ptr long long ptr ptr)
@ stdcall clGetProgramInfo(ptr long long ptr ptr)
@ stdcall clGetSamplerInfo(ptr long long ptr ptr)
@ stdcall clGetSupportedImageFormats(ptr int64 long long ptr ptr)
@ stdcall clLinkProgram(ptr long ptr ptr long ptr ptr ptr ptr)
@ stdcall clReleaseCommandQueue(ptr)
@ stdcall clReleaseContext(ptr)
@ stdcall clReleaseDevice(ptr)
@ stdcall clReleaseEvent(ptr)
@ stdcall clReleaseKernel(ptr)
@ stdcall clReleaseMemObject(ptr)
@ stdcall clReleaseProgram(ptr)
@ stdcall clReleaseSampler(ptr)
@ stdcall clRetainCommandQueue(ptr)
@ stdcall clRetainContext(ptr)
@ stdcall clRetainDevice(ptr)
@ stdcall clRetainEvent(ptr)
@ stdcall clRetainKernel(ptr)
@ stdcall clRetainMemObject(ptr)
@ stdcall clRetainProgram(ptr)
@ stdcall clRetainSampler(ptr)
@ stdcall clSetCommandQueueProperty(ptr int64 long ptr)
@ stdcall clSetEventCallback(ptr long ptr ptr)
@ stdcall clSetKernelArg(ptr long long ptr)
@ stdcall clSetMemObjectDestructorCallback(ptr ptr ptr)
@ stdcall clSetUserEventStatus(ptr long)
@ stdcall clUnloadCompiler()
@ stdcall clUnloadPlatformCompiler(ptr)
@ stdcall clWaitForEvents(long ptr)
