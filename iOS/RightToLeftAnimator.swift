//
//  RightToLeftAnimator.swift
//
//  Created by xyz on 2017/9/22.
//

import Foundation

@objc class RightToLeftAnimator: NSObject, UIViewControllerAnimatedTransitioning {

    func transitionDuration(using transitionContext: UIViewControllerContextTransitioning?) -> TimeInterval {
        return 0.3
    }

    func animateTransition(using transitionContext: UIViewControllerContextTransitioning) {
        let fromVC = transitionContext.viewController(forKey: UITransitionContextViewControllerKey.from)
        let toVC = transitionContext.viewController(forKey: UITransitionContextViewControllerKey.to)
        let containerView = transitionContext.containerView;

        let fromView = transitionContext.view(forKey: UITransitionContextViewKey.from)
        let toView = transitionContext.view(forKey: UITransitionContextViewKey.to)

        let containerFrame = containerView.frame
        var toViewStartFrame = transitionContext.initialFrame(for: toVC!)
        var fromViewStartFrame = transitionContext.initialFrame(for: fromVC!)


        var toViewFinalFrame = transitionContext.initialFrame(for: toVC!)

        var fromViewFinalFrame = transitionContext.initialFrame(for: fromVC!)

        let isPresenting: Bool = toVC?.presentingViewController == fromVC

        //设置动画开始时view的位置
        if (isPresenting) {
            toViewStartFrame.origin.x = containerFrame.size.width
            toViewStartFrame.origin.y = containerFrame.origin.y
            toView?.frame = toViewStartFrame

            fromViewFinalFrame.origin.x = -containerFrame.size.width
            fromViewFinalFrame.origin.y = containerFrame.origin.y
        } else {
            fromViewFinalFrame.origin.x = containerFrame.size.width
            fromViewFinalFrame.origin.y = containerFrame.origin.y

            toView?.frame.origin.x = -containerFrame.size.width
            toView?.frame.origin.y = containerFrame.origin.y
            toViewFinalFrame = containerFrame

        }
        containerView.addSubview(toView!)
        fromView?.frame = containerFrame


        UIView.animate(
            withDuration: self.transitionDuration(using: transitionContext),
            animations: {
                //设置动画结束后view的位置
                if (isPresenting) {
                    toView?.frame = containerFrame
                    fromView?.frame = fromViewFinalFrame
                } else {
                    fromView?.frame = fromViewFinalFrame
                    toView?.frame = toViewFinalFrame
                }
            },
            completion: { (finished) in
                let success = !transitionContext.transitionWasCancelled

                if ((isPresenting && !success) || (!isPresenting && success)) {
                    toView?.removeFromSuperview()
                }
                // Notify UIKit that the transition has finished
                transitionContext.completeTransition(success)
        })
    }

    func animationEnded(_ transitionCompleted: Bool) {
    }
}
